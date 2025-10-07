<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4.4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 07:08:47 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6NDI6MDkgUE07MjU4MQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDc6MDg6NDcgUE07MzsyNjk3"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, A" type="Real" array="False" size=""/>
            <declare name="inte, year, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest(%):&quot;" newline="True"/>
            <input variable="inte"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i &lt; year">
                <assign variable="A" expression="money+(money*inte)/100"/>
                <assign variable="money" expression="A"/>
                <output expression="&quot;Year &quot;&amp;i+1&amp;&quot;: &quot;&amp;A" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>