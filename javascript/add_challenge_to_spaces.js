//Import dependcies
const fs = require("fs");
const YAML = require("js-yaml");

//import actions
const { postQuestion } = require("./js_actions.js");

try {
	const raw = fs.readFileSync("../topics.yaml");
	const data = YAML.load(raw);
	const lengthOfYAMLfile = Object.values(data).length;
	const latestQuestion = data[lengthOfYAMLfile];
	postQuestion(latestQuestion, lengthOfYAMLfile);
} catch (err) {
	console.log(err);
}
