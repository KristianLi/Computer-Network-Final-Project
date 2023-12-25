import { createRouter, createWebHistory } from 'vue-router';
import Chinamap from '../components/Chinamap.vue';
import chinamap from "@/components/chinamap.vue";
import AnalysisLayout from '../components/AnalysisLayout.vue'; // 新的父组件

const routes = [
    { path: '/', component: chinamap },
    { path: '/analysis', component: AnalysisLayout }, // 更新这一行
    { path: '/map', component: Chinamap }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
