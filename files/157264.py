<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="&#3588;&#3619;&#3633;&#3657;&#3591;&#3607;&#3637;&#3656; 1 &#3586;&#3657;&#3629; 4"/>
        <attribute name="authors" value="tpath"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 12:21:05 AM"/>
        <attribute name="created" value="dHBhdGg7Tk9QOzIwMjUtMDctMTY7MTA6NDE6MDcgUE07MjA2Mg=="/>
        <attribute name="edited" value="dHBhdGg7Tk9QOzIwMjUtMDctMTc7MTI6MjE6MDUgQU07MjsyMTU1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="year, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="1"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i &lt;= year">
                <assign variable="money" expression="money*(1+(interest/100))"/>
                <output expression="&quot;Year &quot; &amp;i &amp;&quot;: &quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>