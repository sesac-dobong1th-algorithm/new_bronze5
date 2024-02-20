{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Red\n",
      "Green\n"
     ]
    }
   ],
   "source": [
    "def determine_color(wavelength): # 함수 determine_color 이름 정의, 파장을 입력받음\n",
    "    if wavelength >= 620: # 만약 파장이 620보다 크면 RED 출력\n",
    "        return \"Red\"\n",
    "    elif wavelength >= 590: # 또는 파장이 590 이상이면 ORANGE\n",
    "        return \"Orange\"\n",
    "    elif wavelength >= 570: # 또는 570 이상인 경우 YELLOW\n",
    "        return \"Yellow\"\n",
    "    elif wavelength >= 495: # 파장이 495 이상이면 GREEN\n",
    "        return \"Green\"\n",
    "    elif wavelength >= 450: # 450 이상이면 BLUE\n",
    "        return \"Blue\"\n",
    "    elif wavelength >= 425: # 425 이상이면 INDIGO 출력 (RETURN은 반환이지만 출력으로 이해가 됨)\n",
    "        return \"Indigo\"\n",
    "    else:\n",
    "        return \"Violet\" # 모든 조건들이 해당 안돼면 VIOLET\n",
    "# 함수정의 =======================================\n",
    "\n",
    "wavelength = int(input().strip())    # INPUT - 문자열 입력받음, STRIP - 양쪽공백제거처리\n",
    "print(determine_color(wavelength)) # 출력 - det~함수 호출, 입력값 파장에 따라 별의 색상 출력\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
