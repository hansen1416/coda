<script>
import axios from "axios";

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

			axios
				.post(import.meta.env.VITE_API_URL + "auth/register", data)
				.then((response) => {
					if (response.data) {
						if (response.data.error) {
							this.error = response.data.error;

							setTimeout(() => {
								this.error = "";
							}, 5000);
						} else if (response.data.access_token) {
							localStorage.setItem(
								"jwt",
								response.data.access_token
							);

							window.location = "#/";
						}
					} else {
						this.error = "wrong response format";

						setTimeout(() => {
							this.error = "";
						}, 5000);
					}
				});
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
