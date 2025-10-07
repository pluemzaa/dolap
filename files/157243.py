<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4_3"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 10:16:43 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MzQ6MjUgUE07MjU4MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6NDk6NDYgUE07MTsyNjk3"/>
        <attribute name="edited" value="Tk9OR05FVztERVNLVE9QLThNUk5PM0c7MjU2OC0wNy0xNjsxMDoxNjo0MyBQTTs1OzMwMjM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money" type="Real" array="False" size=""/>
            <declare name="years, i, interest" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i &lt; years">
                <assign variable="money" expression="money *(1+(interest/100))"/>
                <output expression="&quot;Year &quot; &amp; (i+1) &amp; &quot;: &quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>