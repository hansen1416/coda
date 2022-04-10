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
				.post(import.meta.env.VITE_API_URL + "/auth/register", data)
				.then((response) => {
					console.log(response);
				});
		},
	},
};
</script>
<template>
	<div>
		<h3>register</h3>
		<div>
			<label>Username: <input v-model="username" type="text" /></label>
		</div>
		<div>
			<label>Email: <input v-model="email" type="text" /></label>
		</div>
		<div>
			<label
				>Password: <input v-model="password" type="password"
			/></label>
		</div>
		<button @click="register">Submite</button>
	</div>
</template>
