import { createApp } from "vue";
import { createRouter, createWebHashHistory } from "vue-router";
import App from "./App.vue";
import { VuesticPlugin } from "vuestic-ui"; //(✓)
import "vuestic-ui/dist/vuestic-ui.css"; //(✓)

import NotFound from "./NotFound.vue";
import Home from "./Home.vue";
import Login from "./Login.vue";
import Register from "./Register.vue";
import CreateBoard from "./CreateBoard.vue";
import Board from "./Board.vue";
import Thread from "./Thread.vue";

const routes = [
	{ path: "/", component: Home },
	{ path: "/register", component: Register },
	{ path: "/login", component: Login },
	{ path: "/create/board", component: CreateBoard },
	{ path: "/board/:id", component: Board },
	{ path: "/:pathMatch(.*)", component: NotFound },
	{ path: "/thread/:id", component: Thread },
];

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
	// 4. Provide the history implementation to use. We are using the hash history for simplicity here.
	history: createWebHashHistory(),
	routes, // short for `routes: routes`
});

const app = createApp(App);
app.use(router);
app.use(VuesticPlugin); //(✓)
app.mount("#app");
