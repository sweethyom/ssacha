<template>
  <div>
  <NavBar />
  <RouterView />
  </div>
</template>
<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue';
</script>
<style>
  body {
      background-color: black; /* 전체 배경을 검정색으로 설정 */
      color: white; /* 기본 텍스트 색상 */
  }
</style>
