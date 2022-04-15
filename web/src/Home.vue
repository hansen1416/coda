<script>
import axios from "axios";
import { http_request } from "./helpers.js";

export default {
	data() {
		return {
			user: {},
			username: "",
			error: "",
		};
	},
	created() {
		const jwt = localStorage.getItem("jwt");

		if (jwt) {
			http_request(
				"get",
				"auth/me",
				(data) => {
					this.user = JSON.parse(data.current_user);
					this.username = this.user.username;
				},
				this
			);
		}
	},
};
</script>
<template>
	<div>
		<h2>home</h2>
		<p v-if="username">Welcome {{ username }}</p>
		<p></p>
	</div>
</template>
