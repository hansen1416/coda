<script>
import axios from "axios";

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

			axios
				.post(import.meta.env.VITE_API_URL + "auth/login", data)
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
			<va-input label="Email:" v-model="useremail" />
			<va-input label="Password:" type="password" v-model="password" />
		</va-form>
		<va-button type="submit" @click="login">Login</va-button>
	</div>
</template>
