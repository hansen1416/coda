<script>
import axios from "axios";
import { http_request } from "./helpers.js";

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

			http_request(
				"post",
				"board/create",
				(data) => {
					console.log(data);
				},
				this,
				data
			);
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
