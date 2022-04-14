<script>
import axios from "axios";

export default {
	data() {
		return {
			board_name: "",
			error: "",
		};
	},
	methods: {
		create() {
			const data = new FormData();

			data.append("board_name", this.board_name);

			const jwt = localStorage.getItem("jwt");

			axios
				.request({
					method: "post",
					url: import.meta.env.VITE_API_URL + "board/create",
					headers: { Authorization: "Bearer " + jwt },
					data: data,
				})
				.post(import.meta.env.VITE_API_URL + "board/create", data)
				.then((response) => {
					console.log(response);
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
			<va-input label="Board Name:" v-model="board_name" />
		</va-form>
		<va-button type="submit" @click="create">Create</va-button>
	</div>
</template>
