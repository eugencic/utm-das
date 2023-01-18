import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EntranceView from '../views/EntranceView.vue'
import EnglezaView from "../views/EnglezaView.vue";
import InformaticaView from "../views/InformaticaView.vue";
import MatematicaView from "../views/MatematicaView.vue";
import RomanaView from "../views/RomanaView.vue";

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/entrance",
    name: "entrance",
    component: EntranceView,
  },
  {
    path: "/engleza",
    name: "engleza",
    component: EnglezaView,
  },
  {
    path: "/informatica",
    name: "informatica",
    component: InformaticaView,
  },
  {
    path: "/matematica",
    name: "matematica",
    component: MatematicaView,
  },
  {
    path: "/romana",
    name: "romana",
    component: RomanaView,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router