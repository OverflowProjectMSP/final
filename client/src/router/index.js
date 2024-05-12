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
      component: () => import("../components/States/States.vue"),
    },
    {
      path: "/Quetions",
      component: () => import("../components/Main/MainComp.vue"),
    },
    {
      path: "/Login",
      component: () => import("../components/Login/EnterPage.vue"),
    },
    {
      path: "/SignUp",
      component: () => import("../components/Login/RegisterPage.vue"),
    },
    {
      path: "/RecoveryPassPage",
      component: () => import("../components/Login/RecoveryPassPage.vue"),
    },
    {
      path: "/EnterCodePage",
      component: () => import("../components/Login/EnterCodePage.vue"),
    },
    {
      path: "/EnterNewPassword",
      component: () => import("../components/Login/EnterNewPassword.vue"),
    },
    {
      path: "/FAQ",
      component: () => import("../components/FAQ/FAQ.vue"),
    },
    {
      path: "/NewState",
      component: () => import("../components/States/NewState.vue"),
    },
    {
      path: "/TestLanding",
      component: () => import("../components/Landing/LandingPage.vue"),
    },
    
  ],
});
// EnterNewPassword