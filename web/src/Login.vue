<script>
import axios from "axios";

export default {
	data() {
		return {
			emial: "",
			password: "",
		};
	},
	methods: {
		register() {
			const data = new FormData();

			data.append("email", this.email);
			data.append("password", this.password);

			axios
				.post(import.meta.env.VITE_API_URL + "auth/login", data)
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
		<h3>login</h3>
		<div>
			<label>Email: <input v-model="email" type="text" /></label>
		</div>
		<div>
			<label
				>Password: <input v-model="password" type="password"
			/></label>
		</div>
		<button @click="register">Submit</button>
	</div>
</template>
