<template>
  <div>
    <NavBar v-if="!isHeroView" /> <!-- HeroView가 아닐 때만 NavBar 표시 -->
    <RouterView />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { ref, watch } from 'vue';
import NavBar from '@/components/NavBar.vue';

const route = useRoute();
const isHeroView = ref(false); // 반응형 변수로 설정

// 초기 라우트에 따라 isHeroView 설정
isHeroView.value = route.name === 'hero';

// 라우트 변경 감지
watch(() => route.name, (newName) => {
  isHeroView.value = newName === 'hero';
});
</script>

<style>
/* 스타일 추가 */
</style>
<style>
  body {
      background-color: black; /* 전체 배경을 검정색으로 설정 */
      color: white; /* 기본 텍스트 색상 */
  }
</style>