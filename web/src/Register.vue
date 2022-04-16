<script>
import { http_request } from "./helpers.js";

export default {
	data() {
		return {
			username: "",
			useremail: "",
			password: "",
			error: "",
		};
	},
	methods: {
		register() {
			const data = new FormData();

			data.append("username", this.username);
			data.append("email", this.useremail);
			data.append("password", this.password);

			http_request(
				"post",
				"auth/register",
				(data) => {
					localStorage.setItem("jwt", data.access_token);
					localStorage.setItem("jwt_refresh", data.refresh_token);
					window.location = "#/";
				},
				this,
				data
			);
		},
	},
};
</script>
<template>
	<div>
		<va-alert
			v-if="error"
			color="danger"
			border="top"
			border-color="danger"
		>
			{{ error }}
		</va-alert>
		<va-form class="form">
			<va-input label="Username:" v-model="username" />
			<va-input label="Email:" v-model="useremail" />
			<va-input label="Password:" type="password" v-model="password" />
		</va-form>
		<va-button type="submit" @click="register">Register</va-button>
	</div>
</template>
