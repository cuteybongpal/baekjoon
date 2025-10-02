import sys

input = sys.stdin.readline

res = []

#분할 정복
def divide_and_conquer(histogram, start, end):
    #끝과 시작이 같다면 현재 선택된 칸의 길이는 1이기 때문에 히스토그램의 마지막을 리턴해줌
    if end == start:
        return histogram[end]
    #시작과 끝의 차이가 1일 때 히스토그램의 end인덱스가 더 작을 경우, end인덱스의 2를 곱한것과, start 인덱스와 비교해 더 큰 것을 반환함
    #이 경우에는 범위 안에 있는 히스토그램의 개수는 딱 2개 이기 때문에, if문으로 예외 처리한듯
    elif end - start == 1:
        if histogram[end] < histogram[start]:
            return max(2*histogram[end], histogram[start])
        else:
            return max(2*histogram[start], histogram[end])
    
    #중간을 기준으로 나누기
    mid = (start + end) // 2
    #왼쪽의 넓이를 구하기 위해서 자신의 왼쪽을 범위로 재귀함
    left_area = divide_and_conquer(histogram, start, mid)
    #오른쪽의 넓이를 구하기 위해서 자신의 왼쪽을 범위로 재귀함
    right_area = divide_and_conquer(histogram, mid+1, end)
    left = mid-1
    right = mid+1
    #가운데의 넓이는 위에 것만으로 구할 수 없기 때문에 while문을 통해서 구해줌
    mid_area = histogram[mid]
    now_height = histogram[mid]
    
    while start <= left and right <= end:
        #left 인덱스가 더 작을 경우 높이를 right인덱스로 바꾸고, right와 left의 차를 곱해줌(넓이를 구하는 공식임) right 1 증가
        # midarea를 자기 자신과 바꾼 넓이와 비교해, 더 큰 값으로 교체 
        if histogram[left] < histogram[right]:
            if histogram[right] < now_height:
                now_height = histogram[right]
            mid_area = max(mid_area, now_height * (right - left))
            right += 1
        #right 인덱스가 더 작을 경우 높이를 left인덱스로 바꾸고, right와 left의 차를 곱해줌(넓이를 구하는 공식임) left를 1감소
        # midarea를 자기 자신과 바꾼 넓이와 비교해, 더 큰 값으로 교체 
        else:
            if histogram[left] < now_height:
                now_height = histogram[left]
            mid_area = max(mid_area, now_height * (right - left))
            left -= 1
    
    #left로 끝까지 가지 않았을 경우 왼쪽으로 이동 후, 자신과 넓이 비교 후, 더 큰 것으뢰 교체 
    while start <= left:
        if histogram[left] < now_height:
            now_height = histogram[left]
        mid_area = max(mid_area, now_height * (right - left))
        left -= 1
    #right로 끝까지 가지 않았을 경우 오른쪽으로 이동 후, 자신과 넓이 비교 후, 더 큰 것으뢰 교체
    while right <= end:
        if histogram[right] < now_height:
            now_height = histogram[right]
        mid_area = max(mid_area, now_height * (right - left))
        right += 1
    #left_area, right_area, mid_area를 비교해 가장 큰 넓이를 반환
    return max(left_area, right_area, mid_area)
        
            
        
res = []
while True:
    histogram = list(map(int, input().split()))
    
    if histogram[0] == 0: break
    
    n = histogram[0]
    
    res.append(divide_and_conquer(histogram, 1, n))

    
for i in res:
    print(i)