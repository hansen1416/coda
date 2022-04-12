<script>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import Home from "./Home.vue";
import Login from "./Login.vue";
import Register from "./Register.vue";
import NotFound from "./NotFound.vue";

const routes = {
	"/": Home,
	"/register": Register,
	"/login": Login,
};

export default {
	data() {
		return {
			currentPath: window.location.hash,
		};
	},
	computed: {
		currentView() {
			return routes[this.currentPath.slice(1) || "/"] || NotFound;
		},
	},
	mounted() {
		window.addEventListener("hashchange", () => {
			this.currentPath = window.location.hash;
		});
	},
};
</script>

<template>
	<div id="app">
		<va-navbar color="dark" class="nav">
			<template #center>
				<va-navbar-item>
					<a href="#/">Home</a>
				</va-navbar-item>
				<va-navbar-item>
					<a href="#/register">Register</a>
				</va-navbar-item>
				<va-navbar-item>
					<a href="#/login">Login</a>
				</va-navbar-item>
			</template>
		</va-navbar>

		<component :is="currentView" />
	</div>
</template>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
}

.nav a {
	color: #fff;
}

.form {
	width: 600px;
	margin: 30px auto;
}
</style>
