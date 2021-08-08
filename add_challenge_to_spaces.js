//Import dependcies
const fs = require("fs");
const YAML = require("js-yaml");

//import actions
const { postQuestion } = require("./js_actions.js");

try {
	const raw = fs.readFileSync("topics.yaml");
	const data = YAML.load(raw);
	Object.values(data).forEach((item) => {
		if (!item.posted) {
			postQuestion(item);
			item.posted = true;
		}
	});

	let newData = YAML.dump(data);
	fs.writeFileSync("topics.yaml", newData, "utf8");
} catch (err) {
	console.log(err);
}
