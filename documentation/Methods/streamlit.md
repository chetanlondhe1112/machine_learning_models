# Documentation: 

## 1) Streamlit Methods Used in Project

### 1.Streamlit_option_menu
It is similar in function to st.selectbox(), except that:

It uses a simple static list to display the options instead of a dropdown

It has configurable icons for each option item and the menu title

It is built on streamlit-component-template-vue, styled with Bootstrap and with icons from bootstrap-icons.

**Installation**

    pip install streamlit-option-menu

**Parameters**

The option_menu function accepts the following parameters:

*menu_title* (required): the title of the menu.

*options* (required): the array of (string) options to display in the menu

*default_index* (optional, default=0): the index of the selected option by default

*menu_icon* (optional, default=“menu-up”): name of the bootstrap-icon 590 to be used for the menu title

*icons* (optional, default=[“caret-right”]): array of bootstrap-icon 590 names to be used for each option; its length should be equal to the length of options;

The function returns the (string) option currently selected

**Example**

    import streamlit as st
    from streamlit_option_menu import option_menu

    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Settings'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
        selected
