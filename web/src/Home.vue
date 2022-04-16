<script>
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
		const jwt_refresh = localStorage.getItem("jwt_refresh");

		if (jwt_refresh) {
			http_request(
				"get",
				"auth/refresh",
				(data) => {
					localStorage.setItem("jwt", data.access_token);
					localStorage.setItem("jwt_refresh", data.refresh_token);

					this.user = JSON.parse(data.current_user);
					this.username = this.user.username;
				},
				this,
				undefined,
				{ Authorization: "Bearer " + jwt_refresh }
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
