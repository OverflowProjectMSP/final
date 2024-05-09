import { createRouter, createWebHistory } from "vue-router";
export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/:pathMatch(.*)*",
      component: () => import("../components/ReuseComponets/ErrorFour.vue"),
    },
    {
      path: "/",
      component: () => import("../components/Main/MainComp.vue"),
    },
    {
      path: "/States",
      component: () => import("../components/Main/MainComp.vue"),
    },
    {
      path: "/Quetions",
      component: () => import("../components/Main/MainComp.vue"),
    },
  ],
});
