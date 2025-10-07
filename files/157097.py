<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="startend"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:51:52 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NDk6MzkgUE07MjU5MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NTM6MDMgUE07MTsyNjg0"/>
        <attribute name="edited" value="VGhlZXJhcG9uZy1QQzAxO0RFU0tUT1AtVFFCNTFHRTsyNTY4LTA3LTE2OzA2OjUxOjUyIFBNOzE7Mzc4OA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end, i" type="Integer" array="False" size=""/>
            <output expression="&quot;input start number&quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;input end number&quot;" newline="True"/>
            <input variable="end"/>
            <assign variable="i" expression="start"/>
            <while expression="i&lt;=end">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>