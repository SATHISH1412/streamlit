import streamlit as st
import requests

st.set_page_config(page_title="GMS", page_icon="🤖")
backgroud_colour = "backgroud-color: #00FFFF"
st.markdown(f'<style>{backgroud_colour}</style>', unsafe_allow_html=True)

# Function to handle different pages based on the checkbox selection
def Main_List(page):
    if page == "Find the Device":
         findthedevice()
    elif page == "DeviceCount":
        DeviceCountsinglepod()
    elif page == "DeviceCount-2Pods":
        DeviceCounttwopods()
    elif page == "DeviceCount-3Pods":
        DeviceCountthreepods()
    elif page=="DeviceCount-SI":
         DeviceCountsinglepodsi()
    elif page=="DeviceCount-2Pods-SI":
         DeviceCounttwopodssi()
    elif page=="DeviceCount-3Pods-SI":
         DeviceCountthreepodssi()
    elif page == "DeviceList":
        DeviceList()
    elif page == "WebSocket":
        WebSocket()

# Define the content for each page

def DeviceCountsinglepod():
    st.write("## Device Count - Production")
    url1 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response1 = requests.get(url1, verify=False)
    data1 = response1.json()

    result = {
                'podName1': data1['podName'],
                'totalConnected1': int(data1['totalConnected']),
    }

    first_pod = result['podName1']
    first_connection = result['totalConnected1']

    st.write(f' The Pod ID - **{first_pod}** \n')
    st.write(f' The Total Connections - **{first_connection}** \n')
    st.success("Success")
    st.button("Click to refresh!")

def DeviceCounttwopods():
    st.write("## Device Count For 2 Pods - Production")
    url1 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response1 = requests.get(url1, verify=False)
    data1 = response1.json()

    url2 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response2 = requests.get(url2, verify=False)
    data2 = response2.json()

    result = {
                'podName1': data1['podName'],
                'totalConnected1': int(data1['totalConnected']),
                'podName2': data2['podName'],
                'totalConnected2': int(data2['totalConnected']),
            }
    first_pod = result['podName1']
    first_connection = result['totalConnected1']
    second_pod = result['podName2']
    second_connection = result['totalConnected2']
    total_no = result['totalConnected1']+result['totalConnected2']
    device_count = f"Total Connection: **{total_no}**"

    if first_pod != second_pod :
            st.write(f' The 1st Pod ID - **{first_pod}** \n')
            st.write(f' The 1st Pod Connection - **{first_connection}** \n')
            st.write(f' The 2nd pod ID - **{second_pod}** \n')
            st.write(f' The 2nd Pod Connection - **{second_connection}** \n')
            st.success("Success")
            st.write(device_count) 
    else:
            st.warning("Oops! Please refresh again")
        
    st.button("Click to refresh!")

def DeviceCountthreepods():
    st.write("## Device Count For 3 Pods - Production")
    url1 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response1 = requests.get(url1, verify=False)
    data1 = response1.json()

    url2 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response2 = requests.get(url2, verify=False)
    data2 = response2.json()

    url3 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response3 = requests.get(url3, verify=False)
    data3 = response3.json()

    # url4 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/devicecount'
    # response4 = requests.get(url4, verify=False)
    # data4 = response4.json()

    result = {
                'podName1': data1['podName'],
                'totalConnected1': int(data1['totalConnected']),
                'podName2': data2['podName'],
                'totalConnected2': int(data2['totalConnected']),
                'podName3': data3['podName'],
                'totalConnected3': int(data3['totalConnected']),
                # 'podName4': data4['podName'],
                # 'totalConnected4': int(data4['totalConnected']),
            }
    first_pod = result['podName1']
    first_connection = result['totalConnected1']
    second_pod = result['podName2']
    second_connection = result['totalConnected2']
    third_pod = result['podName3']
    third_connection = result['totalConnected3']
    # fourth_pod = result['podName4']
    # fourth_connection = result['totalConnected4']
    total_no = result['totalConnected1']+result['totalConnected2']+result['totalConnected3']
    device_count = f"Total Connection: **{total_no}**"

    if first_pod != second_pod and first_pod!= third_pod and second_pod != third_pod:
            st.write(f' The 1st Pod ID - **{first_pod}** \n')
            st.write(f' The 1st Pod Connection - **{first_connection}** \n')
            st.write(f' The 2nd pod ID - **{second_pod}** \n')
            st.write(f' The 2nd Pod Connection - **{second_connection}** \n')
            st.write(f' The 3rd pod ID - **{third_pod}** \n')
            st.write(f' The 3rd Pod Connection - **{third_connection}** \n \n')
            # st.write(f' The 4th pod ID - **{fourth_pod}** \n')
            # st.write(f' The 4th Pod Connection - **{fourth_connection}** \n \n')
            st.success("Success")
            st.write(device_count) 
    else:
            st.warning("Oops! Please refresh again")
        
    st.button("Click to refresh!")

def DeviceCountsinglepodsi():
    st.write("## Device Count - SI")
    url1 = 'https://gms.comm-mgmt-si.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response1 = requests.get(url1, verify=False)
    data1 = response1.json()

    result = {
                'podName1': data1['podName'],
                'totalConnected1': int(data1['totalConnected']),
    }

    first_pod = result['podName1']
    first_connection = result['totalConnected1']

    st.write(f' The Pod ID - **{first_pod}** \n')
    st.write(f' The Total Connections - **{first_connection}** \n \n')
    st.success("Success \n")
    st.button("Click to refresh!")

def DeviceCounttwopodssi():
    st.write("## Device Count For 2 Pods - SI")
    url1 = 'https://gms.comm-mgmt-si.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response1 = requests.get(url1, verify=False)
    data1 = response1.json()

    url2 = 'https://gms.comm-mgmt-si.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response2 = requests.get(url2, verify=False)
    data2 = response2.json()

    result = {
                'podName1': data1['podName'],
                'totalConnected1': int(data1['totalConnected']),
                'podName2': data2['podName'],
                'totalConnected2': int(data2['totalConnected']),
            }
    first_pod = result['podName1']
    first_connection = result['totalConnected1']
    second_pod = result['podName2']
    second_connection = result['totalConnected2']
    total_no = result['totalConnected1']+result['totalConnected2']
    device_count = f"Total Connection: **{total_no}**"

    if first_pod != second_pod :
            st.write(f' The 1st Pod ID - **{first_pod}** \n')
            st.write(f' The 1st Pod Connection - **{first_connection}** \n')
            st.write(f' The 2nd pod ID - **{second_pod}** \n')
            st.write(f' The 2nd Pod Connection - **{second_connection}** \n')
            st.success("Success")
            st.write(device_count) 
    else:
            st.warning("Oops! Please refresh again")
        
    st.button("Click to refresh!")



def DeviceCountthreepodssi():
    st.write("## Device Count For 3 Pods - SI")
    url1 = 'https://gms.comm-mgmt-si.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response1 = requests.get(url1, verify=False)
    data1 = response1.json()

    url2 = 'https://gms.comm-mgmt-si.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response2 = requests.get(url2, verify=False)
    data2 = response2.json()

    url3 = 'https://gms.comm-mgmt-si.aws.delta.com/gmscore/v1/retrieve/devicecount'
    response3 = requests.get(url3, verify=False)
    data3 = response3.json()

    # url4 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/devicecount'
    # response4 = requests.get(url4, verify=False)
    # data4 = response4.json()

    result = {
                'podName1': data1['podName'],
                'totalConnected1': int(data1['totalConnected']),
                'podName2': data2['podName'],
                'totalConnected2': int(data2['totalConnected']),
                'podName3': data3['podName'],
                'totalConnected3': int(data3['totalConnected']),
                # 'podName4': data4['podName'],
                # 'totalConnected4': int(data4['totalConnected']),
            }
    first_pod = result['podName1']
    first_connection = result['totalConnected1']
    second_pod = result['podName2']
    second_connection = result['totalConnected2']
    third_pod = result['podName3']
    third_connection = result['totalConnected3']
    # fourth_pod = result['podName4']
    # fourth_connection = result['totalConnected4']
    total_no = result['totalConnected1']+result['totalConnected2']+result['totalConnected3']
    device_count = f"Total Connection: **{total_no}**"

    if first_pod != second_pod and first_pod!= third_pod and second_pod != third_pod:
            st.write(f' The 1st Pod ID - **{first_pod}** \n')
            st.write(f' The 1st Pod Connection - **{first_connection}** \n')
            st.write(f' The 2nd pod ID - **{second_pod}** \n')
            st.write(f' The 2nd Pod Connection - **{second_connection}** \n')
            st.write(f' The 3rd pod ID - **{third_pod}** \n')
            st.write(f' The 3rd Pod Connection - **{third_connection}** \n \n')
            # st.write(f' The 4th pod ID - **{fourth_pod}** \n')
            # st.write(f' The 4th Pod Connection - **{fourth_connection}** \n \n')
            st.success("Success")
            st.write(device_count) 
    else:
            st.warning("Oops! Please refresh again")
        
    st.button("Click to refresh!")

def DeviceList():
    st.write("## Device List")
    device_list_1 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/alldevices'
    device_list_2 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/alldevices'
    device_list_3 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/alldevices'
    get_response_1 = requests.get(device_list_1, verify=False)
    get_response_2 = requests.get(device_list_2, verify=False)
    get_response_3 = requests.get(device_list_3, verify=False)
    result_1 = get_response_1.json()
    result_2 = get_response_2.json()
    result_3 = get_response_3.json()
    result = {
                'podName1': result_1['server'],
                'podName2': result_2['server'],
                'podName3': result_3['server'],
            }
    first_pod = result['podName1']
    second_pod = result['podName2']
    third_pod = result['podName3']
    
    if first_pod != second_pod and first_pod!= third_pod and second_pod != third_pod:
        con_result_1 = result_1["sessionData"]
        con_result_2 = result_2["sessionData"]
        con_result_3 = result_3["sessionData"]

        for item in con_result_1:
            values = item["deviceId"]
            ip = item["clientIP"]
            st.write(values)
        for item in con_result_2:
            values = item["deviceId"]
            ip = item["clientIP"]
            st.write(values)
        for item in con_result_3:
            values = item["deviceId"]
            ip = item["clientIP"]
            st.write(values)
            with open('Devicelist.csv') as f:
                st.download_button('Download CSV', values)
    else:
        st.button("Click to refresh!")
            #st.write(ip)
            # st.download_button('Download Device', result_all)
        # Add your content for Page 2 here

def WebSocket():
    st.write("## WebSocket Summary")
    url1 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/websocketsummary'
    response1 = requests.get(url1, verify=False)
    data1 = response1.json()

    url2 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/websocketsummary'
    response2 = requests.get(url2, verify=False)
    data2 = response2.json()

    url3 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/websocketsummary'
    response3 = requests.get(url3, verify=False)
    data3 = response3.json()

    result = {
                'podName1': data1['server'],
                'podName2': data2['server'],
                'podName3': data3['server'],
            }
    first_pod = result['podName1']
    second_pod = result['podName2']
    third_pod = result['podName3']

    if first_pod != second_pod != third_pod:
         st.write(data1)
         st.write(data2)
         st.write(data3)
    else:
            st.warning("Oops! Please refresh again")
            st.button("Click to refresh!") 

def findthedevice():
    st.write("## Find the Device")
    st.write("Enter the Device ID")
    device_id = st.text_input("Device ID")
    url1 = 'https://gms.comm-mgmt-prd.aws.delta.com/gmscore/v1/retrieve/alldevices'
    get_response = requests.get(url1, verify=False)
    result = get_response.json()
    con_result = result["sessionData"]
    for item in con_result:
        values = item["deviceId"]
        ip = item["clientIP"]
        if values == device_id:
            st.write(values)
            st.write(ip)
            st.write("Device found")
        else:
            st.write("Device not found")
    st.button("Search again") 

# Main Streamlit app
def main():
    st.title("Gate Monitor Suite")
    
    # Checkbox to select the page
    page_choice = st.sidebar.radio("# Select a option:", ["DeviceCount","DeviceCount-2Pods","DeviceCount-3Pods","DeviceCount-SI","DeviceCount-2Pods-SI","DeviceCount-3Pods-SI", "DeviceList", "WebSocket","Find the Device"])
    
    # Render the selected page
    Main_List(page_choice)

if __name__ == "__main__":
    main()
