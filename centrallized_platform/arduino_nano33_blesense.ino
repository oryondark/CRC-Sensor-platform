/*
 * 13:proximity
 * 14:Colors
 * 8:Temperature
 * 9:Humidity
 */

#include <Arduino_APDS9960.h>
#include <Arduino_HTS221.h>
#include <Arduino_LSM9DS1.h>
#include <ArduinoJson.h> // generate json.
unsigned long tempTime;
unsigned long humiTime;
unsigned long proxTime;
unsigned long colorTime;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!APDS.begin()) {
    Serial.println("Error initializing APDS9960 sensor.");
  }
  if (!HTS.begin()){
    Serial.println("Error initializing HTS221 sensor.");
  }


}

void loop() {
  StaticJsonDocument<3000> sensing;
  StaticJsonDocument<500> rgbColor;
  StaticJsonDocument<500> temp_sensing;
  StaticJsonDocument<500> humi_sensing;
  StaticJsonDocument<500> proxi_sensing;


  float temperature = HTS.readTemperature();
  float humidity    = HTS.readHumidity();
  float proximity = APDS.readProximity();
  int r, g, b;
  APDS.readColor(r, g, b);
  //colorTime = millis();

  // check if a color reading is available
  while (! APDS.colorAvailable()) {
    delay(5);
  }
  while (! APDS.proximityAvailable()) {
    delay(5);
  }


  JsonArray color_sensor = sensing.createNestedArray("color_sensor");
  JsonArray temp_sensor = sensing.createNestedArray("temp_sensor");
  JsonArray humi_sensor = sensing.createNestedArray("humi_sensor");
  JsonArray proxi_sensor = sensing.createNestedArray("proxi_sensor");


  //collect color sensor data
  JsonArray rgb = rgbColor.createNestedArray("rgbValue");
  JsonArray sensorID_a = rgbColor.createNestedArray("sensorID");
  JsonArray colorTime = rgbColor.createNestedArray("timestamp");

  rgb.add(r);
  rgb.add(g);
  rgb.add(b);
  sensorID_a.add("rgbSensor");
  colorTime.add(String(millis()));
  color_sensor.add(rgbColor);

  //collect temperature sensor data
  JsonArray temp = temp_sensing.createNestedArray("temperature");
  JsonArray sensorID_b = temp_sensing.createNestedArray("sensorID");
  JsonArray tempTime = temp_sensing.createNestedArray("timestamp");

  temp.add(String(temperature));
  sensorID_b.add("temperatureSensor");
  tempTime.add(String(millis()));
  temp_sensor.add(temp_sensing);

  //collect humidity sensor data
  JsonArray humi = humi_sensing.createNestedArray("humidity");
  JsonArray sensorID_c = humi_sensing.createNestedArray("sensorID");
  JsonArray humiTime = humi_sensing.createNestedArray("timestamp");

  humi.add(String(humidity));
  sensorID_c.add("humiditySensor");
  humiTime.add(String(millis()));
  humi_sensor.add(humi_sensing);

  //collect proximity sensor data
  JsonArray proxi = proxi_sensing.createNestedArray("proximity");
  JsonArray sensorID_d = proxi_sensing.createNestedArray("sensorID");
  JsonArray proxiTime = proxi_sensing.createNestedArray("timestamp");

  proxi.add(String(proximity));
  sensorID_d.add("proximitySensor");
  proxiTime.add(String(millis()));
  proxi_sensor.add(proxi_sensing);

  serializeJson(sensing, Serial);

  // print an empty line
  Serial.println();

  // wait a bit before reading again
  delay(3000);
}
