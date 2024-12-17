<template>
  <div>
    <div class="relative bg-gradient-to-r from-purple-600 to-blue-600 h-screen text-white overflow-hidden">
      <div class="absolute inset-0">
        <img src="/img/temporaryImage.png" alt="Background Image" class="object-cover object-center w-full h-full" />
        <div class="absolute inset-0 bg-black opacity-50"></div>
      </div>
      
      <div class="relative z-10 flex flex-col justify-center items-center h-full text-center">
        <h1 class="text-5xl font-bold leading-tight mb-4 transition-all duration-500 ease-in-out">당신의 생각을 공유하고, 새로운 시각을 만나다. <br></h1>
        <p class="text-lg text-gray-300 mb-8 transition-all duration-500 ease-in-out">지금 로그인하고 시작하세요.</p>
        <a href="#" class="bg-slate-700 text-white hover:bg-slate-500 py-2 px-6 rounded-full text-lg font-semibold transition duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg">로그인</a>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100..900&display=swap');

/* scoped 스타일로 폰트 적용 */
h1, p, a {
  font-family: 'Noto Sans KR', sans-serif;
}

/* 로딩 시 전환 효과 */
h1, p {
  opacity: 0; /* 초기 상태에서 투명하게 설정 */
  transform: translateY(20px); /* 아래에서 올라오는 효과 */
  animation: fadeInUp 0.5s forwards; /* 애니메이션 적용 */
}

/* 애니메이션 정의 */
@keyframes fadeInUp {
  to {
    opacity: 1; /* 최종 상태에서 불투명하게 설정 */
    transform: translateY(0); /* 원래 위치로 이동 */
  }
}

/* 반응형 디자인을 위한 스타일 */
@media (max-width: 768px) {
  h1 {
    font-size: 3rem; /* 작은 화면에서 h1 크기 조정 */
  }
  p {
    font-size: 1.25rem; /* 작은 화면에서 p 크기 조정 */
  }
}

@media (max-width: 480px) {
  h1 {
    font-size: 2.5rem; /* 더 작은 화면에서 h1 크기 조정 */
  }
  p {
    font-size: 1rem; /* 더 작은 화면에서 p 크기 조정 */
  }
}
</style>