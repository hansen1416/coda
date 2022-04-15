<script>
import { http_request } from "./helpers.js";

export default {
	data() {
		return {
			useremail: "",
			password: "",
			error: "",
		};
	},
	methods: {
		login() {
			const data = new FormData();

			data.append("email", this.useremail);
			data.append("password", this.password);

			http_request(
				"post",
				"auth/login",
				(data) => {
					localStorage.setItem("jwt", data.access_token);
					localStorage.setItem("jwt_refresh", data.refresh_token);
					window.location = "#/";
				},
				this,
				data
			);

			return;
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
			<va-input label="Email:" v-model="useremail" />
			<va-input label="Password:" type="password" v-model="password" />
		</va-form>
		<va-button type="submit" @click="login">Login</va-button>
	</div>
</template>
