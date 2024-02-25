
def determine_color(wavelength): # 함수 determine_color 이름 정의, 파장을 입력받음
    if wavelengh >= 620: # 만약 파장이 620보다 크면 RED 출력
        return "Red"
    elif wavelength >= 590: # 또는 파장이 590 이상이면 ORANGE
        return "Orange"
    elif wavelength >= 570: # 또는 570 이상인 경우 YELLOW
        return "Yellow"
    elif wavelength >= 495: # 파장이 495 이상이면 GREEN
        return "Green"
    elif wavelength >= 450: # 450 이상이면 BLUE
        return "Blue"
    elif wavelength >= 425: # 425 이상이면 INDIGO 출력 (RETURN은 반환이지만 출력으로 이해가 됨)
        return "Indigo"
    else:
        return "Violet" # 모든 조건들이 해당 안돼면 VIOLET
   # 함수정의 =======================================
    
wavelength = int(input().strip())    # INPUT - 문자열 입력받음, STRIP - 양쪽공백제거처리
print(determine_color(wavelength)) # 출력 - det~함수 호출, 입력값 파장에 따라 별의 색상 출력