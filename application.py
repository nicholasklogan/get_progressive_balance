import main


def handler(event, context):
    return {
  "payload": {
    "google": {
      "expectUserResponse": False,
      "richResponse": {
        "items": [
          {
            "simpleResponse": {
              "textToSpeech": main.format_results(main.get_progressive_balance())
            }
          }
        ]
      }
    }
  }
}