<script>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup

export default {
	data() {
		return {};
	},
};
</script>

<template>
	<div id="app">
		<va-navbar color="dark" class="nav">
			<template #center>
				<va-navbar-item>
					<router-link to="/">Home</router-link>
				</va-navbar-item>
				<va-navbar-item>
					<router-link to="/register">Register</router-link>
				</va-navbar-item>
				<va-navbar-item>
					<router-link to="/login">Login</router-link>
				</va-navbar-item>
				<va-navbar-item>
					<router-link to="/create/board">Create Board</router-link>
				</va-navbar-item>
				<va-navbar-item>
					<router-link to="/create/board">Create Board</router-link>
				</va-navbar-item>
			</template>
		</va-navbar>

		<router-view></router-view>
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
