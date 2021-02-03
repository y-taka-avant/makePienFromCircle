# makePienfromCircle

![out](https://user-images.githubusercontent.com/78395651/106711835-719ab500-663b-11eb-91ec-00facd25fd3f.gif)

## Overview

This is a simple OpenCV Application using a Haugh-Gradient method.
You can convert a circle caputured by your camera to Peading Face(It is called "Pien" in Japan).

これはOpenCVのハフ変換を使った簡単なアプリケーションです。
カメラに映った円形を全てぴえんに変形するものです。

## Reqirement

- Python 3.7.7
- numpy 1.18.5
- OpenCV 3.4.2

## How to Start

```bash
git clone https://github.com/y-taka-avant/makePienFromCircle.git
cd makePienFromCircle-main
python3 main.py
```

if you don't have opencv-python package, install from this command.
```bash 
pip install opencv-python
```

## Usage

Connect a camera(also a Webcam) to your PC.
When start the application, you display something circular like balls, watches, rings and so on.

PCにカメラを繋いでください。標準搭載のWebカメラでも大丈夫です。
アプリを起動したら円形のものにかざしてください。

## Author

[twitter](https://twitter.com/LabAvant)

## Licence

[MIT Licence](https://github.com/y-taka-avant/makePienFromCircle/blob/main/LICENSE)
