<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lap4_4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 07:03:32 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6NDI6MDggUE07MjU4MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDc6MDM6MzIgUE07NzsyNjkw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, service" type="Real" array="False" size=""/>
            <declare name="year, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="1"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="service"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i &lt;= year">
                <assign variable="money" expression="money * (1 + (service / 100))"/>
                <output expression="&quot;Year &quot;&amp; i &amp;&quot;: &quot;&amp;money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>