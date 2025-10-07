<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="PC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 06:32:15 PM"/>
        <attribute name="created" value="UEM7REVTS1RPUC03Q0U2R0tEOzI1NjgtMDctMTk7MDU6NDI6MzYgUE07MjQ5MQ=="/>
        <attribute name="edited" value="UEM7REVTS1RPUC03Q0U2R0tEOzI1NjgtMDctMTk7MDY6MzI6MTUgUE07NjsyNjAx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Money" type="Real" array="False" size=""/>
            <declare name="Year, i, interest" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="Money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="Year"/>
            <while expression="i&lt;Year">
                <assign variable="money" expression="money*(interest/100+(1))"/>
                <output expression="&quot;Year&quot;&amp;i+1&amp;&quot;:&quot;&amp;Money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>