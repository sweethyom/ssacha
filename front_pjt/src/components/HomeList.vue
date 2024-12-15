<template>
  <div class="home-list">
    <div class="live-section">
      <HomeListLiveList :liveItems="liveItems" />
    </div>
    <div class="video-section">
      <HomeListVideoList :videoItems="videoItems" />
    </div>
  </div>
</template>

<script setup>
import HomeListLiveList from '@/components/HomeListLiveList.vue';
import HomeListVideoList from '@/components/HomeListVideoList.vue';
import { ref } from 'vue';

const liveItems = ref([
  { title: '라이브 뉴스 1', viewers: 700 },
  { title: '라이브 뉴스 2', viewers: 987 },
]);

const videoItems = [
  { title: '짧은 비디오 1', duration: '02:10' },
  { title: '짧은 비디오 2', duration: '03:12' },
  { title: '짧은 비디오 3', duration: '01:45' },
  { title: '짧은 비디오 4', duration: '04:20' },
  { title: '짧은 비디오 5', duration: '02:30' },
  { title: '짧은 비디오 6', duration: '03:45' },
  { title: '짧은 비디오 7', duration: '01:50' },
  { title: '짧은 비디오 8', duration: '02:15' },
  { title: '짧은 비디오 9', duration: '03:00' },
  { title: '짧은 비디오 10', duration: '04:10' },
  { title: '짧은 비디오 11', duration: '02:20' },
];
</script>

<style scoped>
.home-list {
  /* padding: 40px; 여백을 늘려서 더 여유롭게 */
  background-color: rgba(0, 0, 0, 0.8); /* 검정색 배경과 투명도 추가 */
  border-radius: 0; /* 모서리 둥글게 제거 */
  box-shadow: none; /* 그림자 제거 */
  width: 100%; /* 전체 너비 사용 */
  color: #fff; /* 텍스트 색상을 흰색으로 변경 */
}

.site-title {
  font-size: 2.5rem; /* 글씨 크기 조정 */
  font-weight: bold; /* 두껍게 */
  color: #fff; /* 텍스트 색상을 흰색으로 변경 */
  text-align: left; /* 왼쪽 정렬 */
  margin-bottom: 30px; /* 아래 여백 */
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); /* 텍스트 그림자 */
}

.video-title {
  font-size: 1.5rem; /* 비디오 리스트 제목 크기 */
  font-weight: bold; /* 약간 두껍게 */
  color: #fff; /* 텍스트 색상을 흰색으로 변경 */
  /* margin-bottom: 20px; 아래 여백 */
  text-align: left; /* 왼쪽 정렬 */
}

.live-section, .video-section {
  /* background-color: rgba(255, 255, 255, 0.1); 각 섹션의 배경색을 반투명 흰색으로 변경 */
  /* border-radius: 10px; 모서리 둥글게 */
  /* padding: 20px; 내부 여백 */
  /* box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5); 부드러운 그림자 */
  margin-bottom: 30px; /* 섹션 간 여백 */
}
</style>