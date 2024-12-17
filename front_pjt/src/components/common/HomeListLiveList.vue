<template>
  <div class="w-full"> <!-- 전체 너비를 사용하도록 설정 -->
    <div id="default-carousel" class="relative z-10" data-carousel="static">
      <!-- Carousel wrapper -->
      <div class="relative min-h-112 md:min-h-144" data-carousel-inner> <!-- 높이 조정 -->
        <!-- 라이브 아이템 -->
        <div v-for="(item, index) in liveItems" :key="item.title" class="duration-700 ease-in-out" :data-carousel-item>
          <div class="live-list">
            <h2 class="text-xl font-bold">라이브 뉴스 목록</h2>
            <div class="live-item">
              <div class="tags">
                <span class="tag title">{{ item.title }}</span>
                <span class="tag viewers">{{ item.viewers }}명 시청 중</span>
              </div>
            </div>
          </div>
        </div>
        <!-- 비디오 아이템 -->
        <div class="duration-700 ease-in-out" data-carousel-item>
          <img src="https://flowbite.com/docs/images/carousel/carousel-1.svg"
               class="object-cover w-full h-full" alt="Slide 1">
        </div>
        <div class="duration-700 ease-in-out" data-carousel-item>
          <img src="https://flowbite.com/docs/images/carousel/carousel-2.svg"
               class="object-cover w-full h-full" alt="Slide 2">
        </div>
        <div class="duration-700 ease-in-out" data-carousel-item>
          <img src="https://flowbite.com/docs/images/carousel/carousel-3.svg"
               class="object-cover w-full h-full" alt="Slide 3">
        </div>
      </div>
      <!-- Slider controls -->
      <button type="button"
              class="flex absolute top-1/2 left-3 z-40 items-center justify-center w-10 h-10 bg-transparent focus:outline-none transition-transform transform hover:scale-110"
              data-carousel-prev>
        <svg class="w-5 h-5 text-gray-600 transition-colors duration-200 hover:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24"
             xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
        </svg>
      </button>
      <button type="button"
              class="flex absolute top-1/2 right-3 z-40 items-center justify-center w-10 h-10 bg-transparent focus:outline-none transition-transform transform hover:scale-110"
              data-carousel-next>
        <svg class="w-5 h-5 text-gray-600 transition-colors duration-200 hover:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24"
             xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps(['liveItems']);
import 'flowbite';
</script>

<style scoped>
.live-list {
  padding: 150px;
  width: 100%; /* 전체 너비 사용 */
}

.live-item {
  margin-bottom: 15px; /* 각 아이템 간 여백 */
}

.tags {
  display: flex;
  gap: 10px; /* 태그 간 간격 */
}

.tag {
  background-color: rgba(255, 255, 255, 0.2); /* 반투명 배경 */
  color: #fff; /* 텍스트 색상 */
  padding: 5px 10px; /* 패딩 */
  border-radius: 5px; /* 둥근 모서리 */
  font-size: 0.9rem; /* 폰트 크기 */
}

/* 전체 배경을 제거하고 이미지가 꽉 차도록 설정 */
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: hidden; /* 스크롤바 제거 */
}

#default-carousel {
  background-color: transparent; /* 배경색 제거 */
}
</style>