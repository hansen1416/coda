<script>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import Home from "./Home.vue";
import Register from "./Register.vue";
import NotFound from "./NotFound.vue";

const routes = {
	"/": Home,
	"/register": Register,
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
		<div class="nev">
			<a href="#/">Home</a> | <a href="#/register">Register</a> |
			<a href="#/non-existent-path">Broken Link</a>
		</div>
		<component :is="currentView" />
	</div>
</template>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
}
</style>
