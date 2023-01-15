- 다음의 객체 요구 사항과 문제의 조건을 만족하는 클래스를 작성해주세요.

## 객체 요구 사항
### 리모컨
+ 일반 리모컨을 의미하는 RemoteController class를 만들어 주세요.

#### 변수
+ 리모컨은 전원상태( on / off )를 나타낼 수 있는 power 변수와
+ 제조사 명을 나타내는 manufacturer 변수와
+ 제조일자를 나타내는 date 변수를 가지고 있습니다.
+ 제조일자와 제조사 명은 초기화 시에만 입력받을 수 있습니다.
+ power 변수의 초깃값은 off입니다.

#### 메소드
+ 리모컨은 전원을 켜고 끄는 power() 메소드를 가지고 있고,
+ 리모컨은 현재 상태(power)를 출력하는 print_current_status() 메소드를 가지고 있습니다.
+ 리모컨은 제조사 명과 제조일자를 출력하는 print_product_infomation() 메소드를 가지고 있습니다.

### 에어컨 리모컨
+ 에어컨 리모컨을 의미하는 AirConditionerRemoteController class를 만들어 주세요.
+ AirConditionerRemoteController는 RemoteController를 상속받습니다.

#### 변수
+ 에어컨 리모컨은 온도를 나타내는 temperature 변수를 가지고 있습니다.
+ 온도의 초깃값은 25도 입니다.

#### 메소드
+ 에어컨 리모컨은 온도를 1도 올리는 temperature_up() 메소드와 온도를 1도 내리는 temperature_down() 메소드를 가지고 있습니다.
+ temperature_up()과 temperature_down() 메소드는 실행 시 바뀐 온도를 출력합니다. 
+ 온도는 16도에서 30도 사이에서만 변화할 수 있습니다.
+ 온도가 16도일 경우 temperature_down()은 상태를 변화시키지 않으며, "temperature is already minimum."를 출력합니다.
+ 온도가 30도일 경우 temperature_up()은 상태를 변화시키지 않으며, "temperature is already maximum."를 출력합니다.
+ 온도를 올리고 내리는 temperature_up(), temperatrue_down() 메소드는 power가 off일 경우 상태를 변화시키지 않으며, "please turn on the power."를 출력합니다.
+ print_current_status() 메소드는 전원 상태와 현재 온도를 출력합니다.

## 추가 조건
+ 기재되지 않은 내용은 스스로 판단하여 구현하시면 됩니다.
+ 다음의 실행코드를 입력했을 때 출력결과와 같이 출력되도록 구현해주세요.

### 입출력관련 ###

### 실행코드1 ###
``` 
remoteController = RemoteController(Samsung, 2022.01.12);
remoteController.print_current_status();
remoteController.power();
remoteController.print_current_status();
remoteController.print_product_infomation();

 ```

### 출력결과1 ###
```
Power is off.
Power is on.
Made by Samsung, in 2022.01.12.
```
### 실행코드2 ###
```
airConditionerRemoteController = AirConditionerRemoteController(Lg, 2022.01.12);
airConditionerRemoteController.temperature_up();
airConditionerRemoteController.power();
airConditionerRemoteController.print_current_status();
airConditionerRemoteController.temperature_up();
airConditionerRemoteController.temperature_up();
airConditionerRemoteController.temperature_up();
airConditionerRemoteController.temperature_up();
airConditionerRemoteController.temperature_up();
airConditionerRemoteController.temperature_up();
```

### 출력결과2 ###
```
Please turn on the power.
Power is on. Temperature is 25.
Temperature is 26.
Temperature is 27.
Temperature is 28.
Temperature is 29.
Temperature is 30.
Temperature is already maximum.
```




- class를 작성후 아래 실행코드를 복붙하여 소스코드를 실행 후 출력결과가 동일하게 나오는지 확인하세요.
- 작성한 class를 아래에 적어주세요.
- 본인의 소스코드를 실행한 출력결과를 스크린샷으로 찍어 첨부해주세요