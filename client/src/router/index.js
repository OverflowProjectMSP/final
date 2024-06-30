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
      path: "/NewState",
      component: () => import("../components/States/NewState.vue"),
    },
    {
      path: "/StateItem",
      component: () => import("../components/States/StateItem.vue"),
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
      path: "/Quetions",
      component: () => import("../components/Quetions/Quetions.vue"),
    },
    {
      path: "/NewQuetion",
      component: () => import("../components/Quetions/NewQuetion.vue"),
    },
    {
      path: "/Profile",
      component: () => import("../components/Profile/Profile.vue"),
    },
    {
      path: "/QuestionItem",
      component: () => import("../components/Quetions/QuestionItem.vue"),
    },
    {
      path: "/Forum",
      component: () => import("../components/Forum/Forum.vue"),
    },
    {
      path: "/ForumPage",
      component: () => import("../components/Forum/ForumPage.vue"),
    },
    {
      path: "/ProfileSettings",
      component: () => import("../components/Profile/SettingsProfile.vue"),
    },
    {
      path: "/ChangePassword",
      component: () => import("../components/Profile/ChangePassword.vue"),
    },
    {
      path: "/UpdateQuestion",
      component: () => import("../components/Quetions/UpdateQuestion.vue"),
    },
    {
      path: "/UpdateState",
      component: () => import("../components/States/UpdateState.vue"),
    },
    {
      path: "/Test",
      component: () => import("../components/TestComp.vue"),
    },
  ],
});
