<template>
  <div class="video-list">
    <h2 class="text-xl font-bold">짧은 뉴스 목록 (주제별)</h2>
    <div class="relative">
            <!-- Slider controls -->
            <button type="button" @click="prevSlide"
              class="flex absolute top-1/2 left-3 z-40 items-center justify-center w-10 h-10 bg-transparent focus:outline-none transition-transform transform hover:scale-110"
              :disabled="currentIndex === 0" data-carousel-prev>
        <svg class="w-5 h-5 text-gray-600 transition-colors duration-200 hover:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24"
             xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
        </svg>
      </button>
      <div class="overflow-hidden">
        <div class="flex transition-transform" :style="{ transform: `translateX(-${currentIndex * (100 / itemsPerPage)}%)` }">
          <div
            v-for="item in videoItems"
            :key="item.title"
            class="flex-shrink-0 w-full md:w-1/4 p-2"
          >
            <div class="flex flex-col justify-between p-4 border border-gray-300 rounded-lg h-32">
              <span class="video-title font-bold">{{ item.title }}</span>
              <span class="duration text-gray-600">길이: {{ item.duration }}</span>
            </div>
          </div>
        </div>
      </div>
      <button type="button"
              @click="nextSlide"
              class="flex absolute top-1/2 right-3 z-40 items-center justify-center w-10 h-10 bg-transparent focus:outline-none transition-transform transform hover:scale-110"
              data-carousel-next :disabled="currentIndex >= maxIndex">
        <svg class="w-5 h-5 text-gray-600 transition-colors duration-200 hover:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24"
             xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, defineProps } from 'vue';

const props = defineProps(['videoItems']);

const currentIndex = ref(0);
const itemsPerPage = 4; // 한 번에 보여줄 항목 수
const maxIndex = computed(() => Math.ceil(props.videoItems.length / itemsPerPage) - 1);

const nextSlide = () => {
  if (currentIndex.value < maxIndex.value) {
    currentIndex.value++;
  }
};

const prevSlide = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--;
  }
};
</script>

<style scoped>
.video-list {
  @apply p-4 rounded-lg;
  position: relative;
  height: 200px; /* 원하는 높이로 조정 */
}
</style>