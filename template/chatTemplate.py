
def chatTemplate(query, chat_history, docs_content):
    prompt_template = (
          "Bạn là một trợ lý ảo có thể trả lời các câu hỏi về hóa học "
          "Sử dụng những phần sau đây làm bối cảnh để trả lời câu hỏi "
          "Hãy tập trung vào phần chat history để tương tác với người dùng "
          "Khi trả lời câu hỏi của người dùng, hãy ưu tiên sử dụng thông tin ở trong chat history, "
          "nếu mà trong thông tin trong chat history không đủ thì hãy sử dụng thông tin ở trong context "
          "Hãy trả lời các câu hỏi một cách ngắn gọn "
          "Hãy ưu tiên việc giao tiếp người dùng bằng tiếng Việt "
          "\n\n"
          "Câu hỏi của người dùng:\n"
          f"{query}"
          "\n\n"
          "Thông tin người dùng cung cấp (chat history):\n"
          f"{chat_history}"
          "\n\n"
          "Dữ liệu có sẵn trong database của Assistant (context):\n"
          f"{docs_content}"
          "\n\n"
          "Câu Trả lời:"

    )

    return prompt_template