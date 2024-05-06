import { createRouter, createWebHistory } from "vue-router";
export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/:pathMatch(.*)*",
      component: () => import("../components/ReuseComponets/ErrorFour.vue"),
    },
  ],
});
