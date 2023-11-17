# 신경망 안에서의 정보 처리는 결국 부동소수점 수로 나타내므로 연산이 가능하도록 인코딩, 디코딩을 해야한다
# p.84 중간단계(뉴런연산)는 입력값의 특징을 잡아내는 부동소수점 수의 모음인 동시에
# 신경망에서 입력이 최종적으로 출력으로 표현되는 방법을 기술하기 위한 수단으로 데이터 구조를 잡아낸다.
# 신경망에서는 텐서(다차원 배열)를 활용하여 데이터를 구성한다.

# %%
import torch

# 크기가 3인 1차원 텐서를 만들고 값을 1로 채우기
a = torch.ones(3)
a

# 인덱스를 사용하여 값을 읽거나 새로운 값을 대입할 수 있다.
# 겉으로는 숫자 객체의 리스트처럼 보이지만 내부 동작은 완전히 다르다.

# %%

# p.88
# 파이썬 리스트나 튜플 객체는 메모리 공간에서 따로따로 할당 된다.
# 반면 파이토치 텐서나 넘파이 배열은 파이썬 객체가 아닌 언방식된 C 언어의 숫자 타입을 포함한 연속적인 메모리가 할당 된다.

# p.94
# 각 차원에 이름 지정이 가능한 텐서 등장
weights_named = torch.tensor([0.2125, 0.7152, 0.0722], names=["channels"])
weights_named

img_t = torch.randn(3, 5, 5)
img_named = img_t.refine_names(..., "channels", "rows", "colums")
print(img_named.shape, img_named.names)


# %%
