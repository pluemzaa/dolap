<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="winpx"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 08:47:11 PM"/>
        <attribute name="created" value="d2lucHg7TEFQVE9QLTI3SDI3RjBJOzI1NjgtMDctMTY7MDg6MzE6MjAgUE07Mjg0MQ=="/>
        <attribute name="edited" value="d2lucHg7TEFQVE9QLTI3SDI3RjBJOzI1NjgtMDctMTY7MDg6NDc6MTEgUE07MTsyOTU2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, inter, total" type="Real" array="False" size=""/>
            <declare name="years, x" type="Integer" array="False" size=""/>
            <assign variable="x" expression="1"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="inter"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="total" expression="money"/>
            <while expression="years &gt;= x">
                <assign variable="total" expression="total * (1 + (inter/100))"/>
                <output expression="&quot;Year &quot; &amp; x &amp; &quot;: &quot;&amp;  total" newline="True"/>
                <assign variable="x" expression="x + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>