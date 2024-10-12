import gradio as gr

"""
物品复活软件
item_rebirth

作者: [代敬宇]
日期: 2024年10月12日
版权: © 2024 [代敬宇]. 保留所有权利。

本软件提供添加、删除、显示和查找物品的功能。
"""

# 用于存储物品信息的列表
items = []

# 添加物品
def add_item(name, description, contact):
    """
    添加新物品到列表中。

    参数：
    name (str): 物品名称
    description (str): 物品描述
    contact (str): 联系信息

    返回：
    str: 操作结果信息
    """
    global items # 声明 items 为全局变量
    
    # 检查物品名称是否已经存在
    if any(item["name"] == name for item in items):
        # 如果物品名称已存在，返回未能添加消息
        return f"物品 '{name}' 已存在，无法添加！"
    else:
        # 如果物品名称不存在，添加新物品
        new_item = {
            "name": name, 
            "description": description, 
            "contact": contact
        }
        
        items.append(new_item)
        return f"物品 '{name}' 添加成功！"

# 删除物品
def delete_item(name):
    """
    从列表中删除指定名称的物品。

    参数：
    name (str): 要删除的物品名称

    返回：
    str: 操作结果信息
    """
    global items
    
    # 检查物品是否存在
    if any(item["name"] == name for item in items):
        # 删除物品并返回成功消息
        items = [item for item in items if item["name"] != name]
        return f"物品 '{name}' 已删除！"
    else:
        # 如果物品不存在，返回未找到消息
        return f"未找到物品 '{name}'！"

# 显示物品列表
def show_items():
    """
    显示当前列表中的所有物品。

    返回：
    str: 物品列表信息
    """
    if not items:
        return "没有物品可显示。"
    return "\n".join([f"名称: {item['name']}, 描述: {item['description']}, 联系人: {item['contact']}" for item in items])

# 查找物品
def find_item(substring):
    """
    查找指定名称的物品。

    参数：
    name (str): 要查找的物品名称

    返回：
    str: 找到的物品信息或提示信息
    """
    found_items = [item for item in items if substring.lower() in item["name"].lower()]
    if not found_items:
        return f"未找到包含 '{substring}' 的物品！"
    return "\n".join([f"找到物品！名称: {item['name']}, 描述: {item['description']}, 联系人: {item['contact']}" for item in found_items])

# 创建Gradio界面
with gr.Blocks() as demo:
    """
    将上述4个功能创建一个Gradio界面

    内容：
    添加物品，删除物品，显示物品，查找物品
    """
    gr.Markdown("## 物品复活软件")
    gr.Markdown("### v1.0")
    gr.Markdown("### 代敬宇 CS3331软件工程作业")

    with gr.Tab("添加物品"):
        with gr.Row():
            name_input = gr.Textbox(label="物品名称")
            description_input = gr.Textbox(label="物品描述")
            contact_input = gr.Textbox(label="联系人信息")
        add_button = gr.Button("添加物品")
        add_output = gr.Textbox(label="输出", interactive=False)
        add_button.click(add_item, inputs=[name_input, description_input, contact_input], outputs=add_output)

    with gr.Tab("删除物品"):
        delete_input = gr.Textbox(label="物品名称")
        delete_button = gr.Button("删除物品")
        delete_output = gr.Textbox(label="输出", interactive=False)
        delete_button.click(delete_item, inputs=delete_input, outputs=delete_output)

    with gr.Tab("显示物品"):
        show_button = gr.Button("显示所有物品")
        show_output = gr.Textbox(label="物品列表", interactive=False)
        show_button.click(show_items, outputs=show_output)

    with gr.Tab("查找物品"):
        find_input = gr.Textbox(label="物品名称的子字符串")
        find_button = gr.Button("查找物品")
        find_output = gr.Textbox(label="查找结果", interactive=False)
        find_button.click(find_item, inputs=find_input, outputs=find_output)

# 启动Gradio界面
if __name__ == "__main__":
    demo.launch()
