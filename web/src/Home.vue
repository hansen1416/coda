<script>
import axios from "axios";

export default {
	data() {
		return {
			user: {},
			username: "",
		};
	},
	created() {
		const jwt = localStorage.getItem("jwt");

		axios
			.request({
				method: "get",
				url: import.meta.env.VITE_API_URL + "auth/me",
				headers: { Authorization: "Bearer " + jwt },
			})
			.then((response) => {
				this.user = JSON.parse(response.data.current_user);
				this.username = this.user.username;
			});
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
