/*
 * This project referenced Tensorflow Workshop with arduino.
 * If you want to take this code, you should be noticed to me and author.
 * Best regards!
 */

#include <TensorFlowLite.h>
/*
* Required module
*/
#include "tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h"
#include "tensorflow/lite/experimental/micro/micro_error_reporter.h"
#include "tensorflow/lite/experimental/micro/micro_interpreter.h"
#include "tensorflow/lite/schema/schema_generated.h"
#include "tensorflow/lite/version.h"

//#include "common.h"

// sensor device header
#include <Arduino_LSM9DS1.h>
// load model and unit test
#include "crcmodel.h"


// must set up null point.
// low-level languages can adjust memory, but sometimes reference a remained data.

const tflite::Model * model = nullptr; // remove non-validation point
tflite::ErrorReporter* error_reporter = nullptr;
tflite::MicroInterpreter* interpreter = nullptr;
TfLiteTensor* input_tensor = nullptr;
TfLiteTensor* output_tensor = nullptr;

tflite::MicroErrorReporter micro_error_reporter;

// AllOpsResolver will to restore your model.
// If you want fine-tune to your model, It can help using MicroOpResolver
tflite::ops::micro::AllOpsResolver resolver;

// constexpr is a non-static type.
// It will no provision memory.
// constexpr means const type expression.
const int tfareasize = 60*1024;
uint8_t tfarea[tfareasize]; // placeholder like tensorflow.


// In our project a input data format should be made (?, 119, 6)
const int sub_batch_size = 84;
const int sub_batch_group_size = 6;

const char * labels[] = { "punch", "flex" };
#define NUM_OF_LABELS (sizeof(labels) / sizeof(labels[0]));

// load model


// Initiated the device envrionment.
void setup() {
  model = ::tflite::GetModel(crc_model);
  error_reporter = &micro_error_reporter;
  Serial.begin(9600);
  if(!IMU.begin()){
    Serial.println("failure IMU module in your device");
  }

  //read the model flow.
  interpreter = new tflite::MicroInterpreter(model, resolver, tfarea, tfareasize, error_reporter);
  interpreter->AllocateTensors();

  // set up in/output pointer.
  input_tensor = interpreter->input(0);
  output_tensor = interpreter->output(0);


}

int count = 0;
// Runned your task code.
//int sub_batch_num_size = 84 * 6;
//float data[84][6];
float * data = new float[504];
float out_v;
int bytes_size = input_tensor->bytes / sizeof(float);

void loop() {
  /*
      layer = 4
      [
       [ 0, 1, 2, 3],
       [ 4, 5, 6, 7],
       [ 8, 9, 10, 11],
       ...
       [N-3, N-2, N-1, N]
      ]
      = (1, N / layer, 4).
       for exam, layer is 4, (1, 4, 4) in python runtime.

       However, Arduino using CPP runtime, you should be flatten your matrix to bytes array form.
       for exam, layer is 4 then 1 * 4 * 4 , then you can calculate 16 atomics.
       so, you have to build a bytes array on 1-line array, the tf-lite model automated matching point of each dimensional.
  */
  float acc_x, acc_y, acc_z;
  float gyr_x, gyr_y, gyr_z;
  int pos = count * 6;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(acc_x, acc_y, acc_z); // Read Acceleration values
  }
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(gyr_x, gyr_y, gyr_z); // Read Gyroscope values
  }
  data[pos + 0] = acc_x;
  data[pos + 1] = acc_y;
  data[pos + 2] = acc_z;
  data[pos + 3] = gyr_x;
  data[pos + 4] = gyr_y;
  data[pos + 5] = gyr_z;
  if(count == 84){
    Serial.println("Start invocation");
    float * features = data;
    for(int i=0 ; i < bytes_size ; i++){
      input_tensor->data.f[i] = features[i];
    }
    interpreter->Invoke();
    Serial.println("Success Invocation");
    count = 0;

    // You must allocate memory because Arduino not easy operate some of the garbege collection.
    features = nullptr;
    delete [] data;
    data = new float[504];
  }
  Serial.print("Increase count num : ");
  count++;
  Serial.println(count);
  delay(300);

}
