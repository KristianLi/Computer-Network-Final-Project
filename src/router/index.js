import { createRouter, createWebHistory } from 'vue-router';
import chinamap from "../components/chinamap.vue";
import AnalysisLayout from '../components/AnalysisLayout.vue'; // 新的父组件

const routes = [
    { path: '/', component: chinamap },
    { path: '/analysis', component: AnalysisLayout }, // 更新这一行
    { path: '/map', component: chinamap }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
