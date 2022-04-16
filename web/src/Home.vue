<script>
import { http_request } from "./helpers.js";

export default {
	data() {
		return {
			user: {},
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

					this.user = data.current_user;
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
		<div v-if="user.id">
			<span>Welcome! </span>
			<va-avatar :src="user.avartar" size="small" />
			<span>&nbsp;{{ user.username }}</span>
		</div>
	</div>
</template>
