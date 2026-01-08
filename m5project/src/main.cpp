#include <M5Unified.h>

void setup() {
  auto cfg = M5.config();
  M5.begin(cfg);

  // 画面初期化
  M5.Display.clear();
  M5.Display.setTextSize(2);
  M5.Display.setCursor(0, 0);
  M5.Display.printf("USER_NAME: %s\n", USER_NAME);
}

void loop() {}