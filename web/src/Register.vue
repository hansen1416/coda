<script>
import axios from "axios";

export default {
	data() {
		return {
			username: "",
			emial: "",
			password: "",
		};
	},
	methods: {
		register() {
			const data = new FormData();

			data.append("username", this.username);
			data.append("email", this.email);
			data.append("password", this.password);

			axios
				.post(import.meta.env.VITE_API_URL + "auth/register", data)
				.then((response) => {
					localStorage.setItem("jwt", response.data.access_token);

					window.location = "#/";
				});
		},
	},
};
</script>
<template>
	<div>
		<va-form class="form">
			<va-input label="Username:" v-model="username" />
			<va-input label="Email:" v-model="email" />
			<va-input label="Password:" type="password" v-model="password" />
		</va-form>
		<va-button type="submit" @click="register">Register</va-button>
	</div>
</template>
