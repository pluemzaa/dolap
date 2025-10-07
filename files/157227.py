<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_3"/>
        <attribute name="authors" value="winpx"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 08:30:33 PM"/>
        <attribute name="created" value="d2lucHg7TEFQVE9QLTI3SDI3RjBJOzI1NjgtMDctMTY7MDg6MjU6MjUgUE07Mjg0OQ=="/>
        <attribute name="edited" value="d2lucHg7TEFQVE9QLTI3SDI3RjBJOzI1NjgtMDctMTY7MDg6MjY6MDUgUE07MTtjb21wdXRlcjtDUC1DT007MjAyNS0wNy0xNjswNDo0Njo0NSBQTTtsYWIgNCBfIDEuZnByZzs2NzMw"/>
        <attribute name="edited" value="d2lucHg7TEFQVE9QLTI3SDI3RjBJOzI1NjgtMDctMTY7MDg6MzA6MzMgUE07MTsyOTUy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Num1, Num2" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="Num1"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="Num2"/>
            <while expression="Num1 &lt;= Num2">
                <output expression="Num1" newline="True"/>
                <assign variable="Num1" expression="Num1 + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>